
%define		_splash		GNU_cool2

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=13192&id=1
Source0:	http://www.kde-look.org/content/files/13192-GNU_cool2-trans.tar.gz
# Source0-md5:	e858e0e8f3f5d01ed27c3e2f6f9d4a50
#Source1:	http://www.kde-look.org/content/download.php?content=13192&id=2
Source1:	http://movingideasanimation.com/dylan/themes/GNU_cool2.tar.gz
# Source1-md5:	102b32c1cf0bab53e4a57c2589e92984
URL:		http://www.kde-look.org/content/show.php?content=13192
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Another splash for KDE with nice graphics from gnu.org.
Inspired by "GNU Cool" theme.

%description -l pl
Kolejny ekran startowy KDE oparty na ³adnej grafice z gnu.org.
Zainspirowany przez motyw "GNU Cool".

%prep
%setup -q -c %{_splash} -n %{_splash} -a1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}-trans \
           $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install %{_splash}-trans/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}-trans
install %{_splash}/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/*
