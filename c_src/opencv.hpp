/*
 * Copyright 2010-2011, Sikuli.org
 * Released under the MIT License.
 *
 */
#ifndef _OPENCV_HPP
#define _OPENCV_HPP

#include<cv.h>
#include<cxcore.h>
#include<highgui.h>

#include<opencv2/features2d.hpp>

#ifdef __APPLE__
#include<opencv/nonfree/features2d.hpp>
#elif __linux
#include<opencv2/nonfree/features2d.hpp>
#endif
#endif
