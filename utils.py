def chunkup(list_object,items_per_list):
    """ chunks up list into a list of lists with n items per list"""
    chunked_list = [list_object[i * items_per_list:(i + 1) * items_per_list] for i in range((len(list_object) + items_per_list - 1) // items_per_list )]
    return chunked_list
