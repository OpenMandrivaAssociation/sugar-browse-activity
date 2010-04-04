# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-browse-activity
Version: 115
Release: %mkrel 1
Summary: Browse activity for Sugar
License: GPLv2+
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Browse/Browse-115.tar.bz2

Patch: sugar-browse-activity-115-sugar-456.patch

Requires: python-hulahop >= 0.7.1
Requires: python  
Requires: python-cjson  
Requires: sugar-toolkit >= 0.88.0

BuildRequires: gettext  
BuildRequires: libpython-devel  
BuildRequires: sugar-toolkit >= 0.88.0

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Browse is a Web browser built on Xulrunner and thus uses the same
Gecko rendering engine as Firefox.

%prep
%setup -q -n Browse-115
%patch -p1

%build

rm -f MANIFEST
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot} -name '*.py.orig' -print0 | xargs -0 rm -f
%find_lang org.laptop.WebActivity

%clean
rm -rf %{buildroot}

%files -f org.laptop.WebActivity.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc AUTHORS COPYING

