%define major 0
%define libname %mklibname - %{major}

Summary:	Music Player Daemon Library
Name:		libmpd
Version:	0.14.0
Release:	%mkrel 1 
License:	GPL
Group:		Sound
Url:		http://sarine.nl/libmpd
Source:		http://download.sarine.nl/gmpc-0.15.0/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Libmpd is an a library to easily connect to a mpd server. 
It's wraps around libmpdclient and provides a higher level api. 

%package devel
Summary:	Header files for developing programs with libmpd
Requires:	%{name} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Group:		Development/Libraries

%description devel
libmpd-devel is a sub-package which contains header files and static libraries
for developing program with libmpd.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/%{name}.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc ChangeLog COPYING README
%{_libdir}/libmpd.so.%{major}*

%files devel
%defattr (-,root,root)
%{_libdir}/libmpd.so
%{_libdir}/pkgconfig/libmpd.pc
%{_includedir}/libmpd
