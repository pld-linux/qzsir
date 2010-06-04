%define	rel	beta
Summary:	QZsir is a hungarian card game
Summary(hu.UTF-8):	QZsir egy magyar kártyajáték (zsírozás)
Summary(pl.UTF-8):	Węgierska gra w karty
Name:		qzsir
Version:	1.0.0
Release:	%{rel}.0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://qzsir.googlecode.com/files/%{name}-%{version}-%{rel}.tar.gz
# Source0-md5:	85f82c9cc5711ada12e6697daae149a9
Patch0:		rules_hu.patch
URL:		http://code.google.com/p/qzsir/
BuildRequires:	QtCore-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QZsir is a hungarian card game, the name is "zsírozás".

%description -l hu.UTF-8
QZsir egy magyar kártyajáték (zsírozás).

%description -l pl.UTF-8
Węgierska gra w karty.

%prep
%setup -q -n %{name}-%{version}-%{rel}
%patch0 -p1

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cp -a qzsir $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/translations
cp translations/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/translations

cp -r pics $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%lang(hu) %doc texts/*hu*.txt
%lang(en) %doc texts/*en*.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%lang(hu) %{_datadir}/%{name}/translations/qzsir_hu.qm
%{_datadir}/%{name}/pics
