# Copyright cybertk. kyan.ql.he@gmail.com
{
  'variables': {
    'conditions': [
      ['OS == "linux"', {
        'use_system_freeglut%': 1,
      }, {
        'use_system_freeglut%': 0,
      }],
    ],
  },

  'conditions': [
    ['use_system_freeglut == 1', {
      'targets': [
        {
          'target_name': 'freeglut',
          'type': 'none',
          'link_settings': {
            'libraries': [
              '-lfreeglut',
            ],
          },
        }, # target
      ],
    }, { # else: use_system_freeglut != 1
      'targets': [
        {
          'target_name': 'freeglut',
            # TODO(kyan): Provide shared_library support.
          'type': 'static_library',

          'direct_dependent_settings': {
            'include_dirs': [
              'files/include',
            ],
            'defines': [
              'FREEGLUT_STATIC',
            ],
          }, # direct_dependent_settings

          'msvs_settings': {
            'VCCLCompilerTool': {
              'CompileAs': '1',
              'DisableSpecificWarnings': '4996',
            },
            'VCLibrarianTool': {
              # pragma in code explictly use freeglut_static.lib.
              'OutputFile': '<(PRODUCT_DIR)/lib/freeglut_static.lib',
            }
          }, # msvs_settings

          'include_dirs': [
            'files/include',
          ],

          'sources': [
            'files/src/freeglut_callbacks.c',
            'files/src/freeglut_cursor.c',
            'files/src/freeglut_display.c',
            'files/src/freeglut_ext.c',
            'files/src/freeglut_font.c',
            'files/src/freeglut_font_data.c',
            'files/src/freeglut_gamemode.c',
            'files/src/freeglut_geometry.c',
            'files/src/freeglut_glutfont_definitions.c',
            'files/src/freeglut_init.c',
            'files/src/freeglut_input_devices.c',
            'files/src/freeglut_joystick.c',
            'files/src/freeglut_main.c',
            'files/src/freeglut_menu.c',
            'files/src/freeglut_misc.c',
            'files/src/freeglut_overlay.c',
            'files/src/freeglut_spaceball.c',
            'files/src/freeglut_state.c',
            'files/src/freeglut_stroke_mono_roman.c',
            'files/src/freeglut_stroke_roman.c',
            'files/src/freeglut_structure.c',
            'files/src/freeglut_teapot.c',
            'files/src/freeglut_videoresize.c',
            'files/src/freeglut_window.c',
            'files/src/freeglut_xinput.c',
          ], # sources

          'conditions': [
            [ 'OS == "win"', {
              'defines': [
                'FREEGLUT_STATIC',
                '_LIB',
              ],
              'sources': [
                'files/src/freeglutdll.def',
              ],
            }],
          ], # conditions
        },
      ]
    }], # conditions
  ],
}
