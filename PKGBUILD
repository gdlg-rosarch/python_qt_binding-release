# Script generated with Bloom
pkgdesc="ROS - This stack provides Python bindings for Qt. There are two providers: pyside and pyqt. PySide is released under the LGPL. PyQt is released under the GPL. Both the bindings and tools to build bindings are included from each available provider. For PySide, it is called &quot;Shiboken&quot;. For PyQt, this is called &quot;SIP&quot;. Also provided is adapter code to make the user's Python code independent of which binding provider was actually used which makes it very easy to switch between these."
url='http://ros.org/wiki/python_qt_binding'

pkgname='ros-lunar-python-qt-binding'
pkgver='0.3.3_3'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-pyqt5'
'qt5-base'
'ros-lunar-catkin'
'ros-lunar-rosbuild'
)

depends=('python2-pyqt5'
)

conflicts=()
replaces=()

_dir=python_qt_binding
source=()
md5sums=()

prepare() {
    cp -R $startdir/python_qt_binding $srcdir/python_qt_binding
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

