from camera import Camera

cam = Camera()
cam.open_cam()
print('Setting resolution to default.')
cam.set_default_resolution()
print('Setting all parameters to default values.')
cam.reset_params_to_default()
cam.close_cam()
print('Done.')

