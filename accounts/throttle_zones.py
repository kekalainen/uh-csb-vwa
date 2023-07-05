class BaseThrottleZone:
    def __init__(self, **_config):
        pass

    def get_bucket_key(self, request, _view_func, _view_args, _view_kwargs):
        raise NotImplementedError()


class User(BaseThrottleZone):
    def get_bucket_key(self, request, _view_func, _view_args, _view_kwargs):
        return request.user.username
