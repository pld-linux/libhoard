Summary:	The Hoard Multiprocessor Memory Allocator
Summary(pl):	Hoard - wieloprocesorowa biblioteka zajmuj�ca si� przydzielaniem pami�ci
Name:		libhoard
Version:	2.1.2d
Release:	1
License:	LGPL with special exception
Group:		Libraries
Source0:	http://www.cs.umass.edu/~emery/software/libhoard-2.1.2d.tar.gz
URL:		http://www.hoard.org/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Hoard memory allocator is a fast, scalable, and memory-efficient
memory allocator for shared-memory multiprocessors.

%description -l pl
Hoard to szybka, skalowalna, wydajnie gospodaruj�ca pami�ci�
biblioteka przydzielaj�ca pami�� dla maszyn wieloprocesorowych ze
wsp�ln� pami�ci�.

%prep
%setup -q

%build
%{__make} \
	USE_LINUX=1 \
	LIBSO="%{__cc} -shared -Wl,-soname=libhoard.so -lpthread -ldl" \
	OPTIMIZE="%{rpmcflags} -ffast-math %{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

install libhoard.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains special exception to LGPL
%doc AUTHORS COPYING ChangeLog NEWS README THANKS docs
%attr(755,root,root) %{_libdir}/lib*.so
