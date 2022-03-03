#pragma once

#include <glib/gmacros.h>

#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <poll.h>
#include <limits.h>

// Glib version

#define GLIB_MAJOR_VERSION 2
#define GLIB_MINOR_VERSION 71
#define GLIB_MICRO_VERSION 2

// Platform info

#define G_OS_UNIX
#define G_BYTE_ORDER G_LITTLE_ENDIAN

// Maximums

#define G_MAXSIZE ULONG_MAX
#define G_MAXSSIZE LONG_MAX
#define G_MAXUINT ULONG_MAX
#define G_MAXINT INT_MAX
#define G_MAXULONG ULONG_MAX

#define G_MININT INT_MIN

// Alignment

#define ALIGNOF_GUINT32 4
#define ALIGNOF_GUINT64 8
#define ALIGNOF_UNSIGNED_LONG 8

// Basic integer typedefs

typedef size_t gsize;
typedef long gssize;

typedef intptr_t gintptr;
typedef uintptr_t guintptr;

typedef gssize goffset;

typedef uint64_t guint64;
typedef uint32_t guint32;
typedef uint16_t guint16;
typedef uint8_t guint8;

typedef int64_t gint64;
typedef int32_t gint32;
typedef int16_t gint16;
typedef int8_t gint8;

// Haveflags

#define HAVE_PTHREAD_COND_TIMEDWAIT_RELATIVE_NP
#define HAVE_POSIX_MEMALIGN 1

#define G_HAVE_GINT64 1

// Formats

#define G_GSIZE_FORMAT "lu"
#define G_GINT16_FORMAT "si"
#define G_GUINT16_FORMAT "su"
#define G_GINT32_FORMAT "i"
#define G_GUINT32_FORMAT "u"
#define G_GINT64_FORMAT "lli"
#define G_GUINT64_FORMAT "llu"
#define G_GINT64_MODIFIER "ll"

// Sizeofs

#define SIZEOF_CHAR 1

#define GLIB_SIZEOF_VOID_P 8
#define GLIB_SIZEOF_SIZE_T 8
#define GLIB_SIZEOF_SSIZE_T 8
#define GLIB_SIZEOF_LONG 8

// IDK

#define GETTEXT_PACKAGE "quakc"

#define G_GOFFSET_CONSTANT(n) n ## L
#define G_GINT64_CONSTANT(n) n ## L
#define G_GUINT64_CONSTANT(n) n ## UL
#define GINT_TO_POINTER(n) ((gpointer) (long) (n))
#define GUINT_TO_POINTER(n) ((gpointer) (unsigned long) (n))
#define GPOINTER_TO_UINT(n) ((unsigned long) (gpointer) (n))

// Wha

#define GSIZE_TO_LE(n) ((gsize) (n))
#define GINT32_TO_LE(n) ((gint32) (n))
#define GINT16_TO_LE(n) ((gint16) (n))

// Proxy system definitions

#define GLIB_SYSDEF_POLLIN   =  POLLIN
#define GLIB_SYSDEF_POLLOUT  =  POLLOUT
#define GLIB_SYSDEF_POLLPRI  =  POLLPRI
#define GLIB_SYSDEF_POLLHUP  =  POLLHUP
#define GLIB_SYSDEF_POLLERR  =  POLLERR
#define GLIB_SYSDEF_POLLNVAL =  POLLNVAL

#define G_DIR_SEPARATOR '/'
#define G_SEARCHPATH_SEPARATOR ':'
#define G_DIR_SEPARATOR_S "/"
#define G_SEARCHPATH_SEPARATOR_S ":"

typedef int GPid;

G_END_DECLS

