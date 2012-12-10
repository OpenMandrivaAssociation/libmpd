%define major 1
%define libname %mklibname mpd %{major}
%define develname %mklibname mpd -d

Summary:	Music Player Daemon Library
Name:		libmpd
Version:	11.8.17
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://sarine.nl/libmpd
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(glib-2.0)

%description
Libmpd is an a library to easily connect to a mpd server.
It's wraps around libmpdclient and provides a higher level api.

%package -n %{libname}
Summary:	Music Player Daemon Library
Group:		System/Libraries

%description -n %{libname}
Libmpd is an a library to easily connect to a mpd server.
It's wraps around libmpdclient and provides a higher level api.

%package -n %{develname}
Summary:	Header files for developing programs with libmpd
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < 11.8.17-1

%description -n %{develname}
libmpd-devel is a sub-package which contains header files and libraries
for developing program with libmpd.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libmpd.so.%{major}*

%files -n %{develname}
%doc ChangeLog README
%{_libdir}/libmpd.so
%{_libdir}/pkgconfig/libmpd.pc
%{_includedir}/libmpd-1.0

