export default {
  methods: {
    onChangeLocale (command) {
      this.$i18n.locale = command
      let message = `Current language: ${this.$t('_name')} [ ${this.$i18n.locale} ]`
      if (process.env.VUE_APP_BUILD_MODE === 'PREVIEW') {
        message = [
          `Current language : ${this.$t('_name')} [ ${this.$i18n.locale} ]`,
          'Only provides switching function, no specific language data is configured',
          'Documentation reference：<a class="el-link el-link--primary is-underline" target="_blank" href="https://d2.pub/zh/doc/d2-admin/locales">《国际化 | D2Admin》</a>'
        ].join('<br/>')
      }
      this.$notify({
        title: 'language change',
        dangerouslyUseHTMLString: true,
        message
      })
    }
  }
}
