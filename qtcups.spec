Summary:	QtCUPS - a CUPS interface and library for Qt
Summary(pl):	QtCUPS - interfejs do CUPS i biblioteka dla Qt
Summary(pt_BR):	Cliente lpr grafico para desktops
Name:		qtcups
Version:	2.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://prdownloads.sourceforge.net/projects/cups/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gcc296.patch
Patch1:		%{name}-qt3.patch
Patch2:		%{name}-plugin.patch
Patch3:		%{name}-noi18n.patch
URL:		http://sourceforge.net/projects/cups/
Requires:	cups >= 1.1.3
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	cups-devel
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
QtCups dostarcza obs³ugê CUPS dla aplikacji Qt. Zawiera:
- frontend do CUPS, który mo¿e byæ u¿ywany jak zamiennik lpr, daj±cy
  ³adny graficzny interfejs do ustawieñ drukarki. Interfejs ten pozwala
  u¿ytkownikom ustawiaæ wszystkie mo¿liwe opcje drukarki.
- bibliotekê pozwalaj±c± aplikacjom Qt drukowaæ przez CUPS i ustawiaæ
  opcje drukarki w CUPS. Klasa QCupsPrinter daje ten sam interfejs co
  QPrinter, wiêc potrzebne zmiany w kodzie s± niewielkie w wiêkszo¶ci
  programów.

%description -l pt_BR
Uma interface gráfica baseada no QT para ser usada no lugar do lpr.

%package devel
Summary:	QtCUPS development files
Summary(pl):	Pliki dla programistów QtCUPS
Summary(pt_BR):	Fornece aplicações para Qt com suporte ao CUPS
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
A development library which enables Qt application to print to CUPS
and configure all CUPS printer options. The class QCupsPrinter
provides the same interface as QPrinter, so code changes are small
for most applications.

%description devel -l pt_BR
Bibliotecas de desenvolvimento que permite as aplicações baseadas no Qt
imprimir pelo CUPS e configurar todas as opções das impressoras do CUPS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
