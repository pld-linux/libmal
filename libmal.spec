
Summary:	A library with the functions for malsync distribution
Summary(pl):	TODO
Name:		libmal
Version:	0.31
Release:	1
License:	MPL
Group:		Libraries
Source0:	http://jasonday.home.att.net/code/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	3d1fd0a5ece6de47d55df5829ee8b6a2
URL:		http://jasonday.home.att.net/code/libmal/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions.

%description -l pl
TODO

%package devel
Summary:	Support files necessary to compile applications with libmal
Summary(pl):	Pliki do kompilowania aplikacji u¿ywaj±cych libmal
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers, and support files necessary to compile applications using
libmal.

%description devel -l pl
Pliki nag³ówkowe i inne potrzebne do kompilowania aplikacji
u¿ywaj±cych libmal.

%package static
Summary:	libmal static library
Summary(pl):	Statyczna biblioteka libmal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libmal static library.

%description static -l pl
Statyczna biblioteka libmal.

%prep
%setup -q

%build
%{__aclocal}
%{__libtoolize}
%{__autoheader}
%{__automake}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MPL-1_0.txt
%{_libdir}/libmal.la
%attr(755,root,root) %{_libdir}/libmal.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/libmal.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libmal.a
