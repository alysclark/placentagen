#!/usr/bin/env python
import numpy as np
import SimpleITK as sitk

"""
.. module:: import_and_export_image
  :synopsis: Contains code to read and write different image formats, primarily based on simpleITK.

:synopsis:Contains code to read and write different image formats


"""

def read_nifti(path):
    """
        :Function name: **read_nifti**

        Uses SimpleITK to read in a nifti file.

        :inputs:
           - path: Text object, path to file.

        return:
           - img: A
    """
    img = sitk.ReadImage(path)
    return img

def get_img_array_sitk(img):
    img_array = sitk.GetArrayFromImage(img)
    return img_array

def extract_dicom_metadata_sitk(imagesitk):
    pixel_dimension = imagesitk.GetSize()
    image_position = imagesitk.GetOrigin()
    pixel_spacing = imagesitk.GetSpacing()
    image_orientation = imagesitk.GetDirection()

    print('Pixel dimensions: ', pixel_dimension)
    print('Pixel spacing: ', pixel_spacing)
    print('Image position: ', image_position)
    print('Image orientation: ', image_orientation)

    return {'pix_dim':pixel_dimension, 'pix_space':pixel_spacing, 'im_pos': image_position, 'im_orient': image_orientation }

def sitk_to_numpy(imagesitk,info,axis=1):
    if(len(info['pix_dim'])<=3):
        img_array = sitk.GetArrayFromImage(imagesitk)# this indexes [k,j,i] for 3d images so need to restack
        if(img_array.ndim > 2): #3D need to restack
            img_temp = np.zeros((img_array.shape[2], img_array.shape[1], img_array.shape[0]))
            for i in range(0, img_array.shape[0]):
                for j in range(0, img_array.shape[1]):
                    for k in range(0, img_array.shape[2]):
                        img_temp[k, j, i] = img_array[i, j, k]
            img_array = img_temp
    else:
        img_array = sitk.GetArrayFromImage(imagesitk)# this indexes [k,j,i] for 3d images so need to restack
        img_temp = np.zeros((img_array.shape[3],img_array.shape[2], img_array.shape[1], img_array.shape[0]))
        for i in range(0, img_array.shape[0]):
            for j in range(0, img_array.shape[1]):
                for k in range(0, img_array.shape[2]):
                    for l in range(0,img_array.shape[3]):
                        img_temp[l, k, j, i] = img_array[i, j, k, l]
        img_array = img_temp

    return img_array