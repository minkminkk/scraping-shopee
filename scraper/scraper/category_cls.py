import requests
import json


class ProductCategoryNode:
    def __init__(
            self, 
            id = None, 
            name = None,
            level = None,
            children = []
        ):
        self.id = id
        self.name = name
        self.level = level
        self.children = children


def get_category_tree():
    """Get data of main categories in Shopee based on API

    Response schema (reduced)
    |- data
        |- category_list
            |- catid
            |- name
            |- display_name
            |- children
                |- catid
                |- name
                |- display_name
                |- children
                    |- ...
                |- ...
            |- ...

    Note: Because Shopee API only shows categories up to level 2,
    this is only a simplified implementation of the category tree.
    This should be re-implemented if tree structure from API changes.
    """
    # Response from Shopee API
    response_json = json.loads(requests.get(
        'https://shopee.vn/api/v4/pages/get_category_tree'
    ).text)

    # Define category tree with empty node as root
    root = ProductCategoryNode()

    # Level-1 categories (main)
    for main_json in response_json['data']['category_list']:
        main_id = main_json['catid']
        main_name = main_json['display_name']
        main_node = ProductCategoryNode(
            id = main_id, 
            name = main_name, 
            level = 1,
        )
        root.children.append(main_node)
        
        # Access the newly inserted main category to insert level-2 categories
        cur = root.children[-1] 

        # Level-2 categories
        child_list = []
        for child_json in main_json['children']:
            child_id = child_json['catid']
            child_name = child_json['display_name']
            child_node = ProductCategoryNode(
                id = child_id, 
                name = child_name, 
                level = 2,
            )
            child_list.append(child_node)
        cur.children = child_list

    return root