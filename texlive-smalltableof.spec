Name:		texlive-smalltableof
Version:	20333
Release:	2
Summary:	Create listoffigures etc. in a single chapter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/smalltableof
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smalltableof.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smalltableof.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows you to create a list of figures and list of
tables in a chapter named 'List' that contains separate
sections for each list of figures, tables, etc.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/smalltableof/smalltableof.sty
%doc %{_texmfdistdir}/doc/latex/smalltableof/README
%doc %{_texmfdistdir}/doc/latex/smalltableof/smalltableof-doc-fr.pdf
%doc %{_texmfdistdir}/doc/latex/smalltableof/smalltableof-doc-fr.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
