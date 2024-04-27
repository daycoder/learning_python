import json
from copy import deepcopy
import requests
import pyperclip


class RailNotFound(Exception):
    ...


def traverse(obj,
             function_at_node=None,
             function_at_object=None,
             depth=0,
             path='',
             **params):
    print(f'{". " * depth}{path=}')
    if isinstance(obj, dict):
        if function_at_object:
            function_at_object(obj,
                               **params)
        for key in obj.keys():
            obj[key] = traverse(obj=obj[key],
                                function_at_node=function_at_node,
                                function_at_object=function_at_object,
                                depth=depth + 1,
                                path=f'{path}/{key}',
                                **params)
        return obj

    elif isinstance(obj, list):
        # Don't think it makes sense to run the function against a list
        for index, item in enumerate(obj):
            obj[index] = traverse(obj=item,
                                  function_at_node=function_at_node,
                                  function_at_object=function_at_object,
                                  depth=depth + 1,
                                  path=f'{path}/[{index}]',
                                  **params)
        return obj
    else:
        if function_at_node:
            return function_at_node(obj,
                                    **params)
        else:
            return obj


def replace_strings_in_object(obj,
                              find,
                              replace,
                              **_):

    def replace_string(string,
                       old,
                       new):
        try:
            new_string = string.replace(old, new)
            print(f'Replaced {old} with {new} in "{string}" yielding "{new_string}')
            return new_string
        except AttributeError:
            return string

    traverse(obj,
             function_at_object=replace_string,
             old=find,
             new=replace)


def do_to_rail(qms_response_body,
               title,
               modifier,
               **params):
    targets = []
    try:
        for slot in qms_response_body.get('slots', [qms_response_body]):
            rails = slot.get('childnodes', [])
            for index, rail in enumerate(rails):
                if rail.get('nodetype') == "SECTION" and rail.get('t').strip().casefold() == title.strip().casefold():
                    # Can't call directly here because we're in a loop
                    # and the modifier might change length of slot or rail
                    targets.append(dict(slot=slot,
                                        rail=rail,
                                        obj=rail,  # This is to make recursive modifiers readable
                                        index=index,
                                        **params))
    except AttributeError:
        ...  # Just swallowing it is probably fine here. It's mostly for when title is not a string

    for target in targets:
        modifier(**target)
    if not targets:
        raise RailNotFound(f'Rail not found with title:"{title}"')


def update_ids(obj,
               suffix='X'):
    for key in ['cmsid', 'nodeid', 'id']:
        if key in obj:
            obj[key] = f'{obj[key]}{suffix}'
            

def copy_rail(slot,
              rail,
              index,
              new_title,
              **_):

    new_rail = deepcopy(rail)
    traverse(new_rail,
             function_at_object=update_ids)
    new_rail['t'] = new_title
    slot['childnodes'].insert(index + 1, new_rail)
    print(f'Added new rail: {new_rail}')


def update_rail(rail,
                update,
                **_):
    rail.update(update)
    print(f'Applied update to rail: {update}')



url = 'https://qms.services.skyq.sky.com/content/r29/menu?bookmark=HOME_TILES&company=SKY&device=IPSETTOPBOX&proposition=GLASS&region=GBR&timeoffset=%2B00%3A00'


qms_page = requests.get(url=url).json()


do_to_rail(qms_response_body=qms_page,
           title='apps & inputs',
           modifier=copy_rail,
           new_title='Apps')

visibility_panel = {"visibility": [[{"id": "stb.capable.hdmi.1",
                                     "if": "true"}
                                    ]]
                    }
visibility_puck = {"visibility": [[{"id": "stb.capable.hdmi.1",
                                    "if": "false"}
                                   ]]
                   }

do_to_rail(qms_response_body=qms_page,
           title='apps & inputs',
           modifier=update_rail,
           update=visibility_puck)

do_to_rail(qms_response_body=qms_page,
           title='apps',
           modifier=update_rail,
           update=visibility_puck)

do_to_rail(qms_response_body=qms_page,
           title='apps',
           modifier=replace_strings_in_object,
           find='Apps & inputs',
           replace='Apps')

j = json.dumps(qms_page,
               indent=4)

pyperclip.copy(j)

print(f'The modified QMS page has been copied to you pastebuffer')
