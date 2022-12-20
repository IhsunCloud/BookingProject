from painless.fields import USField


def connect(signal, **kwargs):
    """
    Decorator to connect to a signal.

    Example:
        @connect(post_save, sender=auth.User)
        def printer(sender, instance, **kwargs):
            print 'Saved user', instance
    """

    kwargs.update({
        'weak': False,
        'dispatch_uid': str(USField())
    })

    def wrapper(func):
        signal.connect(func, **kwargs)
        return func
    return wrapper
