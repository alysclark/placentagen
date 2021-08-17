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