%define		plugin		pagelist
Summary:	DokuWiki Pagelist Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20080808
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.chimeric.de/_src/plugin-pagelist.tgz
# Source0-md5:	fd632aca9688a48c682a1ebdfe1e2aba
Source1:	dokuwiki-find-lang.sh
URL:		http://www.dokuwiki.org/plugin:pagelist
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
The Pagelist Plugin does – as its name says – list wiki pages in a
nice way. Besides its function as a stand-alone syntax plugin, it
serves as helper plugin for the Blog, Discussion, Editor, Tag, Task
and Dir plugins.

%prep
%setup -q -n %{plugin}
if [ $(cat VERSION | tr -d -) != %{version} ]; then
	: %%{version} mismatch, should be: $(cat VERSION | tr -d -)
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/conf
