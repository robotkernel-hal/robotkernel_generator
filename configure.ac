#												-*- Autoconf -*-
# Process this file with autoconf to produce a configure script.
#
AC_PREREQ([2.63])

#
# Robotkernel Version and Maintainer are extracted from project.properties file, change
# them there if needed
#
AC_INIT([robotkernel_service_helper], m4_esyscmd_s([git describe --long --dirty --tags]), [Robert Burger <robert.burger@dlr.de>])

AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])

#
# Checks for programs.
#
AC_PROG_INSTALL
m4_ifdef([PKG_PROG_PKG_CONFIG], [PKG_PROG_PKG_CONFIG])
m4_ifdef([PKG_INSTALLDIR], [PKG_INSTALLDIR], [pkgconfigdir='${libdir}/pkgconfig' AC_SUBST([pkgconfigdir])])

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

# Checks for library functions.

AC_CONFIG_FILES([Makefile])

AC_OUTPUT
