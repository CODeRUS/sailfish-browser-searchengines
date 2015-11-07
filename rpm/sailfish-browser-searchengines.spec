Name:       sailfish-browser-searchengines

BuildArch: noarch

Summary:    Additional search engines for Sailfish Browser
Version:    0.0.10
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfish-browser >= 1.1.3.2

%description
Additional search engines for Sailfish Browser: baidu, duckduckgo, startpage, searx, ixquick, swisscows, qwant, Seznam.cz, Hulbee, search.disroot.org

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/mozembedlite/chrome/embedlite/content
cp -r content/* %{buildroot}/usr/lib/mozembedlite/chrome/embedlite/content

%files
%defattr(-,root,root,-)
/usr/lib/mozembedlite/chrome/embedlite/content
