Summary:	-
Summary(pl):	-
Name:		libhoard
Version:	2.1.2d
Release:	1
License:	LGPL with special exception
Group:		Libraries
Source0:	http://www.cs.umass.edu/~emery/software/libhoard-2.1.2d.tar.gz
URL:		http://www.hoard.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

%build
%{__make} USE_LINUX=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains special exception to LGPL
%doc COPYING
