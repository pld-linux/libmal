Summary:	A library with the functions for malsync distribution
Summary(pl):	Biblioteka funkcji dla dystrybucji malsync
Name:		libmal
Version:	0.40
Release:	1
License:	MPL
Group:		Libraries
Source0:	http://jasonday.home.att.net/code/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-lib64.patch
# Source0-md5:	b570bc495101de915f3401d0baaf6b62
URL:		http://jasonday.home.att.net/code/libmal/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pilot-link-devel >= 0.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions.

%description -l pl
libmal to naprawdê tylko wygodna biblioteka funkcji w dystrybucji
malsync Toma Whittakera wraz z kilkoma funkcjami obudowuj±cymi.

%package devel
Summary:	Support files necessary to compile applications with libmal
Summary(pl):	Pliki do kompilowania aplikacji u¿ywaj±cych libmal
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pilot-link-devel >= 0.11

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
%patch0

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
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
%attr(755,root,root) %{_bindir}/malsync
%attr(755,root,root) %{_libdir}/libmal.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmal.so
%{_libdir}/libmal.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libmal.a
