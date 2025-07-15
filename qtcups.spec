Summary:	QtCUPS - a CUPS interface and library for Qt
Summary(pl.UTF-8):	QtCUPS - interfejs do CUPS i biblioteka dla Qt
Summary(pt_BR.UTF-8):	Cliente lpr grafico para desktops
Name:		qtcups
Version:	2.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/cups/%{name}-%{version}.tar.gz
# Source0-md5:	5c3a82d374a3073c0761b8c45519782e
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gcc296.patch
Patch1:		%{name}-qt3.patch
Patch2:		%{name}-plugin.patch
Patch3:		%{name}-noi18n.patch
URL:		http://sourceforge.net/projects/cups/
BuildRequires:	cups-devel
BuildRequires:	qt-devel >= 3:3.0.5
Requires:	cups >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtCups provides CUPS support for Qt applications. It includes:
- a CUPS front-end to be used as a replacement for "lpr", which
  provides a nice graphical interface for print settings. This interface
  allows users to set all possible printer's options.
- a development library which enables Qt application to print to CUPS
  and configure all CUPS printer options. The class QCupsPrinter
  provides the same interface as QPrinter, sot code changes are small
  for most applications.

%description -l pl.UTF-8
QtCups dostarcza obsługę CUPS dla aplikacji Qt. Zawiera:
- frontend do CUPS, który może być używany jak zamiennik lpr, dający
  ładny graficzny interfejs do ustawień drukarki. Interfejs ten pozwala
  użytkownikom ustawiać wszystkie możliwe opcje drukarki.
- bibliotekę pozwalającą aplikacjom Qt drukować przez CUPS i ustawiać
  opcje drukarki w CUPS. Klasa QCupsPrinter daje ten sam interfejs co
  QPrinter, więc potrzebne zmiany w kodzie są niewielkie w większości
  programów.

%description -l pt_BR.UTF-8
Uma interface gráfica baseada no Qt para ser usada no lugar do lpr.

%package devel
Summary:	QtCUPS development files
Summary(pl.UTF-8):	Pliki dla programistów QtCUPS
Summary(pt_BR.UTF-8):	Fornece aplicações para Qt com suporte ao CUPS
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
A development library which enables Qt application to print to CUPS
and configure all CUPS printer options. The class QCupsPrinter
provides the same interface as QPrinter, so code changes are small for
most applications.

%description devel -l pl.UTF-8
Biblioteka umożliwiająca aplikacji Qt drukowanie poprzez CUPS oraz
konfigurowania opcji drukarek CUPS. Klasa QCupsPrinter udostępnia ten
sam interfejs co QPrinter, więc niezbędne zmiany w kodzie większości
aplikacji są niewielkie.

%description devel -l pt_BR.UTF-8
Bibliotecas de desenvolvimento que permite as aplicações baseadas no
Qt imprimir pelo CUPS e configurar todas as opções das impressoras do
CUPS.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--enable-qt3 \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/System,%{_pixmapsdir}}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System/
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtcups
%attr(755,root,root) %{_libdir}/*
%{_datadir}/qtcups/qtcups.*.qm
%{_applnkdir}/System/*.desktop
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/qtcups
%{_includedir}/qtcups/*.h
