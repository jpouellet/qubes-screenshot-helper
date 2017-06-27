%{!?version: %define version %(cat version)}

Name:		qubes-screenshot-helper
Version:	%{version}
Release:	1%{?dist}
Summary:	Save screenshots in a chosen domain instead of Dom0

License:	ISC
URL:		https://github.com/jpouellet/qubes-screenshot-helper

Requires:	qubes-core-dom0
Requires:	qubes-core-dom0-linux
Requires:	coreutils
Requires:	grep
Requires:	zenity
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils

%define _builddir %(pwd)

%description
Save screenshots in a chosen domain instead of Dom0.

%install
install -D qvm-move-to-chosen-vm $RPM_BUILD_ROOT/usr/libexec/qubes/qvm-move-to-chosen-vm
install -D qubes-save-image-in-vm.desktop $RPM_BUILD_ROOT/usr/share/applications/qubes-save-image-in-vm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, root, root, -)
/usr/share/applications/qubes-save-image-in-vm.desktop
%attr(0755, -, -) /usr/libexec/qubes/qvm-move-to-chosen-vm

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
