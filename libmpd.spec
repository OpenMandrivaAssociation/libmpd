%define major 0
%define libname %mklibname mpd %{major}
%define develname %mklibname mpd -d

Summary:	Music Player Daemon Library
Name:		libmpd
Version:	0.16.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Url:		http://sarine.nl/libmpd
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Libmpd is an a library to easily connect to a mpd server. 
It's wraps around libmpdclient and provides a higher level api. 

%package -n %{libname}
Summary:	Music Player Daemon Library
Group:		Sound
Obsoletes:	libmpd

%description -n %{libname}
Libmpd is an a library to easily connect to a mpd server. 
It's wraps around libmpdclient and provides a higher level api. 

%package -n %{develname}
Summary:	Header files for developing programs with libmpd
Requires:	%{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
Group:		Development/Other

%description -n %{develname}
libmpd-devel is a sub-package which contains header files and static libraries
for developing program with libmpd.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/%{name}.la

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr (-,root,root)
%{_libdir}/libmpd.so.%{major}*

%files -n %{develname}
%defattr (-,root,root)
%doc ChangeLog README
%{_libdir}/libmpd.so
%{_libdir}/pkgconfig/libmpd.pc
%{_includedir}/libmpd
