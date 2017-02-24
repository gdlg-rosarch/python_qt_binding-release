Name:           ros-lunar-python-qt-binding
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS python_qt_binding package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/python_qt_binding
Source0:        %{name}-%{version}.tar.gz

Requires:       python-qt5
Requires:       sip
BuildRequires:  python-qt5
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-rosbuild
BuildRequires:  sip

%description
This stack provides Python bindings for Qt. There are two providers: pyside and
pyqt. PySide is released under the LGPL. PyQt is released under the GPL. Both
the bindings and tools to build bindings are included from each available
provider. For PySide, it is called &quot;Shiboken&quot;. For PyQt, this is
called &quot;SIP&quot;. Also provided is adapter code to make the user's Python
code independent of which binding provider was actually used which makes it very
easy to switch between these.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Feb 24 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.2-0
- Autogenerated by Bloom

