Summary:	QtCUPS - a CUPS interface and library for Qt
Summary(pl):	QtCUPS - interfejs do CUPS i biblioteka dla Qt
Name:		qtcups
Version:	1.1
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://download.sourcefoge.net/cups/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/cups
Requires:	cups >= 1.1.3
BuildRequires:	qt-devel >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
QtCups provides CUPS support for Qt applications. It includes:
- a CUPS front-end to be used as a replacement for "lpr", which
  provides a nice graphical interface for print settings. This interface
  allows users to set all possible printer's options.
- a development library which enables Qt application to print to CUPS
  and configure all CUPS printer options. The class QCupsPrinter
  provides the same interface as QPrinter, sot code changes are small
  for most applications.

%description -l pl
QtCups dostarcza obs≥ugÍ CUPS dla aplikacji Qt. Zawiera:
- frontend do CUPS, ktÛry moøe byÊ uøywany jak zamiennik lpr, daj±cy
  ≥adny graficzny interfejs do ustawieÒ drukarki. Interfejs ten pozwala
  uøytkownikom ustawiaÊ wszystkie moøliwe opcje drukarki.
- bibliotekÍ pozwalaj±c± aplikacjom Qt drukowaÊ przez CUPS i ustawiaÊ
  opcje drukarki w CUPS. Klasa QCupsPrinter daje ten sam interfejs co
  QPrinter, wiÍc potrzebne zmiany w kodzie s± niewielkie w wiÍkszo∂ci
  programÛw.

%package devel
Summary:	QtCUPS development files
Summary(pl):	Pliki dla programistÛw QtCUPS
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
QtCUPS development files.

%description devel -l pl
Pliki dla programistÛw QtCUPS.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--enable-qt2 \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtcups
%attr(755,root,root) %{_libdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/qtcups
