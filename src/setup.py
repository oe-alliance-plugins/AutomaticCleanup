from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.AutomaticCleanup'
setup(name='enigma2-plugin-systemplugins-automaticcleanup',
       version='3.0',
       description='Automatic System Cleanup (setting backups, orphaned movie files, timer entries)',
       package_dir={pkg: 'AutomaticCleanup'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'LICENSE']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
