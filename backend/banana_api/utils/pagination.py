from ..exceptions.BadRequestException import BadRequestException

def get_pagination_params(request, default_page=1, default_size=10):
    page = request.GET.get('page', default_page)
    size = request.GET.get('size', default_size)

    try:
        page = int(page)
        size = int(size)
    except ValueError:
        raise BadRequestException("Query parameters 'page' and 'size' must be integers.")

    return page, size