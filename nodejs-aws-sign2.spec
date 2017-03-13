%{?scl:%scl_package nodejs-aws-sign2}
%{!?scl:%global pkg_name %{name}}
%global npm_name aws-sign2

%{?nodejs_find_provides_and_requires}

Name:		%{?scl_prefix}nodejs-aws-sign2
Version:    0.6.0
Release:    1%{?dist}
Summary:	AWS signing.
Url:		http://registry.npmjs.org/aws-sign2/-/aws-sign2-0.5.0.tgz
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ASL 2.0

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%description
AWS signing. Originally pulled from LearnBoost/knox, now a standalone module.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%files
%{nodejs_sitelib}/aws-sign2
%doc README.md LICENSE

%changelog
* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.6.0-1
- Updated with script

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.5.0-4
- rebuilt

* Tue Jul 21 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.5.0-3
- rebuilt

* Mon Jul 20 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.5.0-2
- Fix wrong variable
- moved LICENSE to %%doc for el6

* Thu Jul 16 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.5.0-1
- Initial build
