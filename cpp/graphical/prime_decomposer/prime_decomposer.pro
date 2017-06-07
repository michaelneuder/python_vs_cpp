#-------------------------------------------------
#
# Project created by QtCreator 2017-06-07T13:35:58
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = prime_decomposer
TEMPLATE = app


SOURCES += main.cpp\
        window.cpp \
    prime_factors.cpp

HEADERS  += window.h \
    prime_factors.h

FORMS    += window.ui

#CONFIG   += c++11
QMAKE_CXXFLAGS += -std=c++11
