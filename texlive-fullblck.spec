Name:		texlive-fullblck
Version:	1.03
Release:	1
Summary:	Left-blocking for letter class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fullblck
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Used with the letter documentclass to set the letter in a
fullblock style (everything at the left margin).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/fullblck/README
%doc %{_texmfdistdir}/doc/latex/fullblck/fullblck.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.dtx
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.dtx.asc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}
