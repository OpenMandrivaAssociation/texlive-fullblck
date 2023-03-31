Name:		texlive-fullblck
Version:	25434
Release:	2
Summary:	Left-blocking for letter class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fullblck
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullblck.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Used with the letter documentclass to set the letter in a
fullblock style (everything at the left margin).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fullblck/fullblck.sty
%doc %{_texmfdistdir}/doc/latex/fullblck/README
%doc %{_texmfdistdir}/doc/latex/fullblck/fullblck.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.dtx
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.dtx.asc
%doc %{_texmfdistdir}/source/latex/fullblck/fullblck.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
