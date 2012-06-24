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
QtCups dostarcza obs�ug� CUPS dla aplikacji Qt. Zawiera:
- frontend do CUPS, kt�ry mo�e by� u�ywany jak zamiennik lpr, daj�cy
  �adny graficzny interfejs do ustawie� drukarki. Interfejs ten pozwala
  u�ytkownikom ustawia� wszystkie mo�liwe opcje drukarki.
- bibliotek� pozwalaj�c� aplikacjom Qt drukowa� przez CUPS i ustawia�
  opcje drukarki w CUPS. Klasa QCupsPrinter daje ten sam interfejs co
  QPrinter, wi�c potrzebne zmiany w kodzie s� niewielkie w wi�kszo�ci
  program�w.

%package devel
Summary:	QtCUPS development files
Summary(pl):	Pliki dla programist�w QtCUPS
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	%{name} = %{version}

%description devel
QtCUPS development files.

%description devel -l pl
Pliki dla programist�w QtCUPS.

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
