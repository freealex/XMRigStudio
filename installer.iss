#define MyAppName "XMRigStudio"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "freealex"
#define MyAppExeName "XMRigStudio.exe"

[Setup]
AppId={{A6D8B91E-2C3F-4A9E-9C6A-123456789ABC}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=installer
OutputBaseFilename=XMRigStudio-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "dist\XMRigStudio.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\XMRigStudio"; Filename: "{app}\XMRigStudio.exe"
Name: "{autodesktop}\XMRigStudio"; Filename: "{app}\XMRigStudio.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\XMRigStudio.exe"; Description: "Launch XMRigStudio"; Flags: nowait postinstall skipifsilent
