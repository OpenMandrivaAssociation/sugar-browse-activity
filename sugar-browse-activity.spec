# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-browse-activity
Version: 105
Release: %mkrel 1
Summary: Browse activity for Sugar
License: GPLv2+
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Browse/Browse-105.tar.bz2

Requires: python-hulahop >= 0.4.9
Requires: python  
Requires: python-cjson  
Requires: sugar-toolkit >= 0.84.0

BuildRequires: gettext  
BuildRequires: libpython-devel  
BuildRequires: sugar-toolkit >= 0.84.0

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Browse is a Web browser built on Xulrunner and thus uses the same
Gecko rendering engine as Firefox.

%prep
%setup -q -n Browse-105


%build
python  \
	setup.py \
	build

%install
rm -rf %{buildroot}
[ -f setup.py ] && chmod 0755 setup.py
python  \
	setup.py \
	install \
	--prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.WebActivity

%clean
rm -rf %{buildroot}

%files -f org.laptop.WebActivity.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc AUTHORS COPYING

