%define		_prefix		/usr/X11R6

Summary:	QtCUPS - a CUPS interface and library for Qt
Name:		qtcups
Version:	1.1
Release:	1
Group:		X11/KDE/System
Copyright:	GPL
Source:		http://download.sourcefoge.net/cups/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/cups
Requires:	cups >= 1.1.3
Requires:	qt >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtCups provides CUPS support for Qt applications. It includes :
- a CUPS front-end to be used as a replacement for "lpr", which
  provides a nice graphical interface for print settings. This
  interface allows users to set all possible printer's options.
- a development library which enables Qt application to print to
  CUPS and configure all CUPS printer options. The class QCupsPrinter
  provides the same interface as QPrinter, sot code changes are
  small for most applications.

%package devel
Summary:	QtCUPS development files
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki

%description devel
QtCUPS development files

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--enable-qt2 \
	--with-qt-libraries=%{_prefix}/lib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtcups
%attr(755,root,root) %{_libdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/qtcups
