%define name libmpd
%define version 0.13.0
%define api_version     0.13
%define lib_major       0
%define lib_name        %mklibname - %{api_version} %{lib_major}

Summary: Music Player Daemon Library
Name: %{name}
Version: %{version}
Release: %mkrel 2 
License: GPL
Url: http://cms.qballcow.nl/index.php?page=libmpd
Group: Sound
Source: http://download.qballcow.nl/programs/gmpc-0.13/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description

Libmpd is an a library to easily connect to a mpd server. 
It's wraps around libmpdclient and provides a higher level api. 

%package devel
Summary: Header files for developing programs with libmpd
Requires: %{name} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-%{api_version}-devel
Group: Development/Libraries
Requires: pkgconfig

%description devel
libmpd-devel is a sub-package which contains header files and static libraries
for developing program with libmpd.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc ChangeLog COPYING README
%{_libdir}/libmpd.so.0*

%files devel
%defattr (-,root,root)
%{_libdir}/libmpd.so
%{_libdir}/pkgconfig/libmpd.pc
%{_prefix}/include/libmpd


