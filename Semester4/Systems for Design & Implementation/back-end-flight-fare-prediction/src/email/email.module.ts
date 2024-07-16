import { Module } from '@nestjs/common';

import { MailService } from './email.service';
import { EmailController } from './email.controller';

@Module({
  imports: [],
  controllers: [EmailController],
  providers: [MailService],
  exports: [MailService],
})
export class EmailModule {}
