Name:       sailfish-browser-searchengines

# >> macros
BuildArch: noarch
# << macros

Summary:    Additional search engines for Sailfish Browser
Version:    0.0.8
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfish-browser >= 1.1.3.2

%description
Additional search engines for Sailfish Browser: baidu, duckduckgo, startpage, searx, ixquick, swisscows, qwant, Seznam.cz


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/lib/mozembedlite/chrome/embedlite/content
cp -r content/* %{buildroot}/usr/lib/mozembedlite/chrome/embedlite/content
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
/usr/lib/mozembedlite/chrome/embedlite/content
# >> files
# << files
