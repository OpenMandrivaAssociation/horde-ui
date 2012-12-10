%define prj     Horde_UI

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:		horde-ui
Version:	0.0.2
Release:	%mkrel 3
Summary:	Horde Browser package
License:	LGPL
Group:		Networking/Mail
Url:		http://pear.horde.org/index.php?package=%{prj}
Source0:	%{prj}-%{version}.tgz
BuildArch:	noarch
Requires(pre):  php-pear
Requires:	php-pear-channel-horde
BuildRequires:	php-pear
BuildRequires:	php-pear-channel-horde

%description
The Horde_UI:: class provides an API for getting information about
the current user's userinterface and its capabilities.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%dir %{peardir}/Horde/UI/VarRenderer
%{peardir}/Horde/UI/Language.php
%{peardir}/Horde/UI/Tabs.php
%{peardir}/Horde/UI/Pager.php
%{peardir}/Horde/UI/Widget.php
%{peardir}/Horde/UI/VarRenderer.php
%{peardir}/Horde/UI/VarRenderer/html.php
%{peardir}/Horde/UI/VarRenderer/tableset_html.php



%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-3mdv2011.0
+ Revision: 564106
- Increased release for rebuild

* Sat Feb 20 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 508642
- updated rel
- removed unneeded dependencies

* Fri Feb 19 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 507958
- import horde-ui


