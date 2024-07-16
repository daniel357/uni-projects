/**
 *
 * @param template The current string which has template values like {{value}} inside. Ex. The value is greater than {{value}}.
 * @param values The values which will replace the corresponding templates from the string { value: 3 }
 * @returns The string with template values replaced: "The value is greater than 3."
 */
export const replaceStringTemplateValuesFromObject = (template: string, values?: any): string => {
  if (!values) {
    return template;
  }

  const regex = /{{(.*?)}}/g;

  return template.replace(regex, (_, capture: string) => values[capture] || '');
};
