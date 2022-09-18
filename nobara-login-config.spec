BuildArch:              noarch

Name:          nobara-login-config
Version:       0.1
Release:       1%{?dist}
License:       GPLv2
Group:         System Environment/Libraries
Summary:       GUI Login Selector


URL:           https://github.com/CosmicFusion/nobara-login-config

Source0:        %{name}-%{version}-%{release}.tar.gz

BuildRequires:	wget
Requires:      /usr/bin/bash
Requires:	zenity

%install
tar -xf %{SOURCE0}
mv usr %{buildroot}/
mkdir -p %{buildroot}/usr/share/licenses/nobara-login-config
wget https://raw.githubusercontent.com/CosmicFusion/nobara-login-config/main/LICENSE.md -O %{buildroot}/usr/share/licenses/nobara-login-config/LICENSE

%description
GUI Selector for GDM, SDDM, and LightDM
%files
%attr(0755, root, root) "/usr/bin/nobara-login-config"
%attr(0644, root, root) "/usr/share/licenses/nobara-login-config/LICENSE"
