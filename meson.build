project('fcitx5-table-hiraganify')

python3 = find_program('python3')
libime_tabledict = find_program('libime_tabledict')

fcitx5_core = dependency('Fcitx5Core')
fcitx5_prefix = fcitx5_core.get_variable('prefix')

main_txt = custom_target(
  'hiraganify.main.txt',
  input: ['gen.py'],
  output: 'hiraganify.main.txt',
  command: [python3, '@INPUT0@', '@OUTPUT0@'],
  build_by_default: true)

main_dict = custom_target(
  'hiraganify.main.dict',
  input: [main_txt],
  output: 'hiraganify.main.dict',
  command: [libime_tabledict, '@INPUT0@', '@OUTPUT0@'],
  build_by_default: true,
  install: true,
  install_dir: ['share/fcitx5/table'])

install_data(
  'hiraganify.conf',
  install_dir: 'share/fcitx5/inputmethod')
