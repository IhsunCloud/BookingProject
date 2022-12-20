def upload_directory_path(instance, filename):
    """ file will be uploaded to --> MEDIA_ROOT/file_<id>/<filename> """
    return 'file_{0}/{1}'.format(instance.id, filename)