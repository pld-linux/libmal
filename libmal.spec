Summary:	A library with the functions for malsync distribution
Summary(pl.UTF-8):	Biblioteka funkcji dla dystrybucji malsync
Name:		libmal
Version:	0.44
Release:	6
License:	MPL
Group:		Libraries
Source0:	http://jasonday.home.att.net/code/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	826f2334c8eb24f5e170f208581fdffb
Patch0:		%{name}-lib64.patch
URL:		http://jasonday.home.att.net/code/libmal/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pilot-link-devel >= 0.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions.

%description -l pl.UTF-8
libmal to naprawdę tylko wygodna biblioteka funkcji w dystrybucji
malsync Toma Whittakera wraz z kilkoma funkcjami obudowującymi.

%package devel
Summary:	Support files necessary to compile applications with libmal
Summary(pl.UTF-8):	Pliki do kompilowania aplikacji używających libmal
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pilot-link-devel >= 0.11

%description devel
Headers, and support files necessary to compile applications using
libmal.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne potrzebne do kompilowania aplikacji
używających libmal.

%package static
Summary:	libmal static library
Summary(pl.UTF-8):	Statyczna biblioteka libmal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libmal static library.

%description static -l pl.UTF-8
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
%ghost %{_libdir}/libmal.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmal.so
%{_libdir}/libmal.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libmal.a
