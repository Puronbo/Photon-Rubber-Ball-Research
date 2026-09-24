export const meta = {
  name: 'expert_audit_and_develop',
  description: 'Read a target script, have experts audit it, then produce an improved version',
  phases: [
    { title: 'Read Script', detail: 'Load the target script content' },
    { title: 'Audit', detail: 'Four experts audit code quality, security, performance, documentation' },
    { title: 'Develop', detail: 'Expert synthesizes feedback and produces an improved script' }
  ]
};

const scriptPath = './ai_script_manager_final.py';

phase('Read Script');
const scriptResult = await agent(
  `Read the file at '${scriptPath}' and return its exact content.`,
  {schema: {type: 'string'}}
);
const scriptContent = scriptResult;

phase('Audit');
const auditResults = await parallel(
  [
    () => agent(`Audit the following script for code quality, style, and maintainability. Provide a concise bullet list of issues and suggestions for improvement.\n\nSCRIPT:\n${scriptContent}`, {schema: {type: 'string'}}),
    () => agent(`Perform a security review of the following script. Identify any vulnerabilities, unsafe practices, and recommend mitigations.\n\nSCRIPT:\n${scriptContent}`, {schema: {type: 'string'}}),
    () => agent(`Analyze the performance of the following script. Look for inefficiencies, possible bottlenecks, and suggest optimizations.\n\nSCRIPT:\n${scriptContent}`, {schema: {type: 'string'}}),
    () => agent(`Review the documentation and comments in the following script. Assess clarity, completeness, and suggest improvements.\n\nSCRIPT:\n${scriptContent}`, {schema: {type: 'string'}})
  ]
);

const auditSummary = `
Code Quality:\n${auditResults[0]}
\nSecurity:\n${auditResults[1]}
\nPerformance:\n${auditResults[2]}
\nDocumentation:\n${auditResults[3]}
`;

phase('Develop');
const improvedScript = await agent(
  `You are an expert software engineer. Based on the following audit feedback, produce an improved version of the script. Address all issues raised while preserving the original functionality. Return only the revised script content.\n\nAUDIT FEEDBACK:\n${auditSummary}\n\nORIGINAL SCRIPT:\n${scriptContent}`,
  {schema: {type: 'string'}}
);

return { auditResults: { codeQuality: auditResults[0], security: auditResults[1], performance: auditResults[2], documentation: auditResults[3] }, improvedScript };