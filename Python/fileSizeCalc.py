print('File size calculator in KiB, MiB, GiB')
filetype = input('Enter the type of file: Image (I) or Sound (S): ')

def file_size(x, y, z):
    size = round((x * y * z) / 8)
    print('File Size (byte) = ', round(size))
    print('File Size (KiB) = ', round(size / 1024, 2))
    print('File Size (MiB) = ', round(size / 1024 / 1024, 2))
    print('File Size (GiB) = ', round(size / 1024 / 1024 / 1024, 2))

    print('File Size (KB) = ', round(size / 1000, 2))
    print('File Size (MB) = ', round(size / 1000 / 1000, 2))
    print('File Size (GB) = ', round(size / 1000 / 1000 / 1000, 2))

if filetype == 'I':
    width = int(input('Enter the image width: '))
    height = int(input('Enter the image height: '))
    depth = int(input('Enter the image color depth: '))

    print(file_size(width, height, depth))

elif filetype == 'S':
    duration = int(input('Enter the sound duration: '))
    resolution = int(input('Enter the sound resolution: '))
    hertz = int(input('Enter the hertz rate: '))
  
    print(file_size(duration, resolution, hertz))